import React, { Component } from 'react';
import {Container,Jumbotron,Row, Col, Button} from "react-bootstrap"
import Deliveries from "./Deliveries"
import Workers from "./Workers"
import axios from 'axios';

class LayOut extends Component {
    state = { 
        deliveries:[],
        workers:[]
     }
    
     getDeliveries = () => {
        axios.get('https://delivery-app-backend-x.herokuapp.com/deliveries')
        .then((response) => {
            var deliveries_ = response.data.deliveries;
            console.log(response.data.deliveries)
            var newDeliveries = [];
            for(var delivery of deliveries_){
                console.log(delivery)
                newDeliveries.push({id:delivery.id, status:delivery.status,completionTime:delivery.completionTime})
            }
            this.setState({deliveries:newDeliveries})
          console.log(newDeliveries);
      });
   }

   postDeliveries = () => {
      axios.post('https://delivery-app-backend-x.herokuapp.com/update_deliveries', this.state.deliveries)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
   }

     getWorkers = () => {
          axios.get('https://delivery-app-backend-x.herokuapp.com/workers')
          .then((response) => {
              var workers_ = response.data.workers;
              var newWorkers = [];
              for(var worker of workers_){
                  console.log(worker)
                newWorkers.push({name:worker.name,id:worker.id,status:worker.status})
              }
              this.setState({workers:newWorkers})
            console.log(response);
        });
     }

     postWorkers = () => {
        axios.post('https://delivery-app-backend-x.herokuapp.com/update_workers', this.state.workers)
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
     }

     setWorkerStatus = (workerName,status) => {
         var workersUpdate = this.state.workers;
         var workerToUpdate = workersUpdate.find(worker => worker.name == workerName);
         workerToUpdate.status = status;
        this.setState({workers:workersUpdate});
        this.postWorkers();
     }
     setDeliveryStatus = (deliveryId,status,choosenWorkerName) => {
        var deliveryUpdate = this.state.deliveries;
        var deliveryToUpdate = deliveryUpdate.find(delivery => delivery.id == deliveryId);
        deliveryToUpdate.status = status;
        if(status == "IN PROGRESS"){
            var dateNow = new Date();
            var date = new Date(dateNow.getTime() + Math.round(Math.random() * 2)*60000);
            deliveryToUpdate.completionTime = date.getHours() + ":" + date.getMinutes()
            console.log(choosenWorkerName)
            deliveryToUpdate.choosenWorkerName = choosenWorkerName;
        }
        if(status == "DONE"){
            deliveryToUpdate.completionTime = "";
            deliveryToUpdate.choosenWorkerName = "";
        } 
        
        this.setState({deliveries:deliveryUpdate});
        this.postDeliveries();
    }
    refreshDeliveries = () => {
        var now = new Date();
        for(var delivery of this.state.deliveries){
          if(delivery.choosenWorkerName == "" ||delivery.choosenWorkerName == null ){
            continue;
          }
          
            if(delivery.completionTime.split(":")[0] < now.getHours() ){
              if(delivery.completionTime != "" ||delivery.completionTime != null ){
                this.setWorkerStatus(delivery.choosenWorkerName,"FREE");
              }
                this.setDeliveryStatus(delivery.id,"DONE");
            }
            if(delivery.completionTime.split(":")[0] == now.getHours() ){
                if(delivery.completionTime.split(":")[1] < now.getMinutes()){
                  if(delivery.completionTime != "" ||delivery.completionTime != null ){
                    this.setWorkerStatus(delivery.choosenWorkerName,"FREE");
                  }
                    this.setDeliveryStatus(delivery.id,"DONE");
                }
            }
        }
      this.postDeliveries();
    }

    componentDidMount() {
      //this.intervalRefreshDeliveries = setInterval(() => this.refreshDeliveries(), 1000);
      this.intervalRefreshWorkers = setInterval(() => this.getWorkers(), 2000);
      this.intervalRefreshDeliveries2 = setInterval(() => this.getDeliveries(), 2000);
    }
    componentWillUnmount() {
      //clearInterval(this.intervalRefreshDeliveries);
      clearInterval(this.intervalRefreshWorkers);
      clearInterval(this.intervalRefreshDeliveries2);
      
    }


    render() { 
        return <Jumbotron fluid >
        <Container>
        <Row>
        <Col>
            <h1>Active Delivery</h1>
            <Button style={{marginRight:10}} onClick={() => this.refreshDeliveries()}>Refresh Date</Button>
            <Deliveries setDeliveryStatus={this.setDeliveryStatus} setWorkerStatus={this.setWorkerStatus} workers={this.state.workers} deliveries={this.state.deliveries}/>
        </Col>
        <Col>
        <h1>Active Delivery Workers</h1>    
        <Workers workers={this.state.workers}/>
        </Col>
        </Row>
        </Container>
      </Jumbotron>
    }
}
 
export default LayOut;
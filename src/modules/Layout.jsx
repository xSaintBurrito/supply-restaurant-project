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
              console.log(response.data.workers)
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
         console.log(workerName);
         console.log(this.state.workers)
         var workerToUpdate = workersUpdate.find(worker => worker.name == workerName);
         workerToUpdate.status = status;
        this.setState({workers:workersUpdate});
     }
     setDeliveryStatus = (deliveryId,status) => {
        var deliveryUpdate = this.state.deliveries;
        console.log(deliveryId);
        console.log(this.state.deliveries)
        console.log(status)
        var deliveryToUpdate = deliveryUpdate.find(delivery => delivery.id == deliveryId);
        deliveryToUpdate.status = status;
        if(status == "IN PROGRESS"){
            var dateNow = new Date();
            var date = new Date(dateNow.getTime() + Math.round(Math.random() * 30)*60000);
            deliveryToUpdate.completionTime = date.getHours() + ":" + date.getMinutes()
        }
        if(status == "DONE"){
            deliveryToUpdate.completionTime = "";
        }
        
        this.setState({deliveries:deliveryUpdate});
    }
    refreshDeliveries = () => {
        var now = new Date();
        for(var delivery of this.state.deliveries){
            if(delivery.completionTime.split(":")[0] < now.getHours() ){
                this.setDeliveryStatus(delivery.id,"DONE");
            }
            if(delivery.completionTime.split(":")[0] == now.getHours() ){
                if(delivery.completionTime.split(":")[1] < now.getMinutes()){
                    this.setDeliveryStatus(delivery.id,"DONE");
                }
            }
        }
    }


    render() { 
        return <Jumbotron fluid >
        <Container>
        <Row>
        <Col>
            <h1>Active Delivery</h1>
            <Button style={{marginRight:10}} onClick={() => this.getDeliveries()}>Refresh Deliveries</Button>
            <Button style={{marginRight:10}} onClick={() => this.postDeliveries()}>Post Deliveries</Button>
            <Button style={{marginRight:10}} onClick={() => this.refreshDeliveries()}>Refresh Deliveries</Button>
            <Deliveries setDeliveryStatus={this.setDeliveryStatus} setWorkerStatus={this.setWorkerStatus} workers={this.state.workers} deliveries={this.state.deliveries}/>
        </Col>
        <Col>
        <h1>Active Delivery Workers</h1>
        <Button style={{marginRight:10}} onClick={() => this.getWorkers()}>Refresh Workers</Button>
        <Button style={{marginRight:10}} onClick={() => this.postWorkers()}>Post Workers</Button>
            
        <Workers workers={this.state.workers}/>
        </Col>
        </Row>
        </Container>
      </Jumbotron>
    }
}
 
export default LayOut;
import React, { Component } from 'react';
import {Container,Jumbotron,Row, Col, Button} from "react-bootstrap"
import Deliveries from "./Deliveries"
import Workers from "./Workers"
import axios from 'axios';

class LayOut extends Component {
    state = { 
        deliveries:[455,431,432,423423,4123,1231,24,241,2,3123],
        workers:[]
     }
    
     getWorkers = () => {
          axios.get('/workers')
          .then((response) => {
              var workersZ = response.data.workers;
              console.log(response.data.workers)
              var newWorkers = [];
              for(var worker of workersZ){
                  console.log(worker)
                newWorkers.push({name:worker.name,id:worker.id,status:worker.status})
              }
              this.setState({workers:newWorkers})
            console.log(response);
        });
     }

     postWorkers = () => {
        axios.post('/update_workers', this.state.workers)
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
    render() { 
        return <Jumbotron fluid >
        <Container>
        <Row>
        <Col>
            <h1>Active Delivery</h1>
            <Deliveries setWorkerStatus={this.setWorkerStatus} workers={this.state.workers} deliveries={this.state.deliveries}/>
        </Col>
        <Col>
        <h1>Active Delivery Workers</h1>
        <Button onClick={() => this.getWorkers()}>Refresh Workers</Button>
        <Button onClick={() => this.postWorkers()}>Post Workers</Button>
            
        <Workers workers={this.state.workers}/>
        </Col>
        </Row>
        </Container>
      </Jumbotron>
    }
}
 
export default LayOut;
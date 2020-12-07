import React, { Component } from 'react';
import {Container,Jumbotron,Row, Col} from "react-bootstrap"
import Deliveries from "./Deliveries"
import Workers from "./Workers"

class LayOut extends Component {
    state = { 
        deliveries:[69,431,432,423423,4123,1231,24,241,2,3123],
        workers:[{name:"Matt V",id:233,status:"BUSSY"}
                ,{name:"Zofia S",id:65,status:"FREE"}
                ,{name:"Thomas V",id:323,status:"BUSSY"}
                ,{name:"Alba V",id:897,status:"FREE"}]
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
        <Col><h1>Active Delivery Workers</h1>
        <Workers workers={this.state.workers}/>
        </Col>
        </Row>
        </Container>
      </Jumbotron>
    }
}
 
export default LayOut;
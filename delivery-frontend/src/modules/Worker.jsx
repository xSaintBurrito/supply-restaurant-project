import React, { Component } from 'react';
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"

class Worker extends Component {
    state = {
        workerId:this.props.workerId,
        workerName:this.props.workerName,
        workerStatus:this.props.workerStatus,
        isWorkerBUSY:false
      }
    printWorkerStats = (status) => {
        if(status == "BUSY"){
            return <span style={{color:"red"}}> BUSY</span>
        }
        return <span style={{color:"green"}}> FREE</span>
    }
    render() { 
        return <div style={{width:"100%"}}>
             <span>name:</span><span style={{color:"blue"}}> {this.state.workerName}</span>
        <span> workerId:</span><span style={{color:"blue"}}> {this.state.workerId}</span>
    <span> status: {this.printWorkerStats(this.props.workerStatus)}</span>
        <br></br>
          <hr></hr>
    </div> ;
    }
}
 
export default Worker;
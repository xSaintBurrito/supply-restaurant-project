import React, { Component } from 'react';
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"

class OneDelivery extends Component {
    state = {
        deliveryId:this.props.id,
        deliverStatus:this.props.status,
        choosenWorkerName: "",
      }

      printGetDefaultWorker = (name) => {
          if(this.props.workers.filter(worker => worker.name != name).filter(worker => worker.status == "FREE")[0]){
              console.log(this.props.workers.filter(worker => worker.name != name).filter(worker => worker.status == "FREE")[0])
              return this.props.workers.filter(worker => worker.name != name).filter(worker => worker.status == "FREE")[0].name;
          }
          return "";
      }
    
      printStatus = () => {
        if(this.props.status == "ACTIVE"){
            return <span style={{color:"red"}}>ACTIVE</span>;
        }
        if(this.props.status == "IN PROGRESS"){
            return <span style={{color:"yellow"}}>IN PROGRESS</span>;
        }
        if(this.props.status == "DONE"){
            return <span style={{color:"green"}}>DONE</span>;
        }
      }

      changeStatus = () => {
          if(!this.state.choosenWorkerName){
                if(this.printGetDefaultWorker("") == ""){
                    return;
                }
                var backups = this.printGetDefaultWorker("");
                this.props.setWorkerStatus(backups,"BUSY")
          }
          else{
            this.props.setWorkerStatus(this.state.choosenWorkerName,"BUSY")
          }
          this.props.setDeliveryStatus(this.props.id,"IN PROGRESS",this.state.choosenWorkerName)
          this.setState({deliverStatus:"IN PROGRESS"})
          this.setState({choosenWorkerName:this.printGetDefaultWorker(this.state.choosenWorkerName)})
          console.log(this.props.workers);
          console.log(this.state.choosenWorkerName)
      }

      printActiveMenu = () => {
          if(this.state.deliverStatus == "ACTIVE"){
          return <React.Fragment>
              <br></br>
            <Form.Label style={{display:"inline-block"}}>Who should be put to this order</Form.Label>
            <Form.Control style={{width:"20%"}} as="select" onChange={event => {this.setState({choosenWorkerName:event.target.value});console.log(event.target.value)}}>
                {this.props.workers.filter(worker => worker.status == "FREE").map(worker => <option value={worker.name}>{worker.name}</option>)}
            </Form.Control>
            <br/>
          <Button onClick={() => this.changeStatus()}>Make Delivery</Button>
          </React.Fragment>
          }
          return "";
      }
      
    render() { 
        return <div style={{width:"100%"}}>
        <span>deliveryId:</span><span style={{color:"blue"}}> {this.state.deliveryId}</span>
        <span> status: {this.printStatus()} {this.props.completionTime}</span>
        {this.printActiveMenu()}
          <hr></hr>
    </div> ;
    }
}
 
export default OneDelivery;
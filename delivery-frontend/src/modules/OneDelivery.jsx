import React, { Component } from 'react';
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"

class OneDelivery extends Component {
    state = {
        deliveryId:this.props.id,
        deliverStatus:"ACTIVE"
      }
    
      printStatus = () => {
        if(this.state.deliverStatus == "ACTIVE"){
            return <span style={{color:"red"}}>ACTIVE</span>;
        }
        if(this.state.deliverStatus == "IN PROGRESS"){
            return <span style={{color:"yellow"}}>IN PROGRESS</span>;
        }
        if(this.state.deliverStatus == "IN PROGRESS"){
            return <span style={{color:"green"}}>DONE</span>;
        }
      }

      changeStatus = () => {
          this.setState({deliverStatus:"IN PROGRESS"})
      }

      printActiveMenu = () => {
          if(this.state.deliverStatus == "ACTIVE"){
          return <React.Fragment>
              <br></br>
            <Form.Label style={{display:"inline-block"}}>Who should be put to this order</Form.Label>
            <Form.Control style={{width:"20%"}} as="select">
                {this.props.workers.map(worker => <option>{worker.name}</option>)}
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
        <span> status: {this.printStatus()}</span>
        {this.printActiveMenu()}
          <hr></hr>
    </div> ;
    }
}
 
export default OneDelivery;
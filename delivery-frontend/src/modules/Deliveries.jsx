import React, { Component } from 'react';
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import OneDelivery from "./OneDelivery"
class Deliveries extends Component {
    state = { 
        deliveries: this.props.deliveries
     }
    render() { 
        return  <React.Fragment>
            {this.state.deliveries.map(delivery => <OneDelivery setWorkerStatus={this.props.setWorkerStatus} id={delivery} workers={this.props.workers} />)}
        </React.Fragment>
    }
}
 
export default Deliveries;
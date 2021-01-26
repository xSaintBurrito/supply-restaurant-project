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
            {this.props.deliveries.map(delivery => <OneDelivery setDeliveryStatus={this.props.setDeliveryStatus} setWorkerStatus={this.props.setWorkerStatus} completionTime={delivery.completionTime} status={delivery.status} id={delivery.id} workers={this.props.workers} />)}
        </React.Fragment>
    }
}
 
export default Deliveries;
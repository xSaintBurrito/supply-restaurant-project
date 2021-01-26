import React, { Component } from 'react';
import Navbar from "react-bootstrap/Navbar"


class NavBarDelivery extends Component {
    state = {  }
    render() { 
        return <Navbar bg="light" expand="lg">
          <Navbar.Brand href="#home">Delivery App</Navbar.Brand>
        </Navbar>
    }
}
 
export default NavBarDelivery;
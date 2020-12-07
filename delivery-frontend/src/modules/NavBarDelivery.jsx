import React, { Component } from 'react';
import Navbar from "react-bootstrap/Navbar"


class NavBarDelivery extends Component {
    state = {  }
    render() { 
        return <Navbar bg="light" expand="lg">
          <Navbar.Brand href="#home">Delivery App</Navbar.Brand>
          {/* <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#link">Link</Nav.Link> */}
        </Navbar>
    }
}
 
export default NavBarDelivery;
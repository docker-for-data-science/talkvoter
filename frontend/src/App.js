import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import {
  Container, Row, Col,
  Navbar, NavbarBrand, Nav,
  UncontrolledDropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import VoteCard from './components/VoteCard';

import './App.css';

class Foo extends Component {
  render() {
    return (
      <div>
        <h2>Page Foo</h2>
      </div>
    );
  }
}

const NavigationBar = () => (
  <Navbar color="dark" dark expand="md">
    <NavbarBrand className="mx-auto" href="/">
      <div className="navbar-title">Talk Recommender</div>
    </NavbarBrand>

    <Nav navbar>
      <UncontrolledDropdown nav inNavbar>
        <DropdownToggle nav caret></DropdownToggle>
        <DropdownMenu right>
          <DropdownItem tag={Link} to="/">Vote</DropdownItem>
          <DropdownItem tag={Link} to="/predict">Predict</DropdownItem>
          <DropdownItem divider />
          <DropdownItem href="/login">Login</DropdownItem>
          <DropdownItem href="/logout">Logout</DropdownItem>
        </DropdownMenu>
      </UncontrolledDropdown>
    </Nav>
  </Navbar>
)

const Content = () => (
  <Container>
    <Row>
      <Col>
        <Switch>
          <Route exact path="/" component={VoteCard} />
          <Route path="/predict" component={Foo} />
        </Switch>
      </Col>
    </Row>
  </Container>
)

const Layout = () => (
  <Router>
    <div>
      <NavigationBar />
      <br />
      <Content />
    </div>
  </Router>
)

class App extends Component {
  render() {
    return (
      <Layout />
    );
  }
}

export default App;

import React, { Component } from 'react';
import {
  Card, CardBody, CardFooter, CardTitle, CardSubtitle, CardText,
  Button } from 'reactstrap';

class RecommendationList extends Component {
  constructor(props) {
    super(props);
    this.state = {talks: []}
    this.getTalkRecommendations();
  }

  getTalkRecommendations() {
    /*
    Hit Flask endpoint to get talk recommendations for current year
    */
    fetch('/api/v1/predict/', {
      method: 'GET',
      headers: {'Content-Type': 'application/json'},
      credentials: "same-origin",
    })
    .then(response => response.json())
    .then(response => this.setState({talks : response['predicted_talks']}));
  }

  renderCard(talks){
    return (
    talks.map( talk =>
      <Card>
        <CardBody>
          <CardTitle tag="h3" className="text-center">{talk['title']}</CardTitle>
          <CardSubtitle className="text-center">
            <small>Presented by: {talk['presenters']}</small><br />
            <small>Location: {talk['location']}</small>
          </CardSubtitle>
          <br />
          <CardText>{talk['description']}</CardText>
        </CardBody>
      </Card>
      )
    );
  }

  render() {
    let talks = this.state.talks;
    if (talks !==undefined && talks.length == 95){
      return (
      <div>
        <h3>Looks like you don't like missing out anything! Please <a href="/">filter some more to watch later!</a></h3>
        { this.renderCard(talks) }
      </div>
      );
    } else {
      return(
      <div>
      <h3>Found {talks.length} talks to watch in person. Try <a href="/">filtering more</a> if you want better results.</h3>
        { this.renderCard(talks) }
      </div>
      );
    }
  }
}

export default RecommendationList;

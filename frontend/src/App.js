import React from 'react';
import { Card, CardBody, CardFooter, CardTitle, CardSubtitle, CardText} from 'reactstrap';
import { Container, Row, Col } from 'reactstrap';
import { Button } from 'reactstrap';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        result: {},
        talk_id: null,
    };
    this.fetchRandomTalk()
  }

  fetchRandomTalk() {
    /*
    Hit Flask endpoint to get talk from last year that user has not voted on
    */
    fetch('http://app:8000/api/v1/talks/random/', {method: 'GET'})
    .then(function(response) {
      response.json()
    })
    .then(data => this.setState({
      result: data,
      talk_id: data['id'],
    }));
  }

  vote(event, vote_type) {
    /*
    Process vote user vote and load next talk
    */
    event.preventDefault();

    let body_ = {
      "vote": null
    };

    if (vote_type === 'yes') {
      body_['vote'] = 'in_person'
    } else {
      body_['vote'] = 'watch_later'
    }

    let that = this;  // this trick never fails :D

    fetch('http://app:8000/api/v1/talks/' + this.state.talk_id + '/vote/', {
        method: 'POST',
        body: JSON.stringify(body_),
        headers: {'Content-Type': 'application/json'},
    }).then(function(response) {
      if (response.status === 200) {
        that.fetchRandomTalk();
      }
    });
  }

  render() {
    return (
      <Container>
        <Row>
          <Col>
            <Card>
              <CardBody>
                <CardTitle tag="h3" className="text-center">{this.state.result['title']}</CardTitle>
                <CardSubtitle className="text-center"><small>Presented by: {this.state.result['presenters']}</small></CardSubtitle>
                <br />
                <CardText>{this.state.result['description']}</CardText>
              </CardBody>
              <CardFooter>
                <Row>
                  <Col>
                    <Button color="danger" onClick={(e) => this.vote(e, 'no')}>Watch Later</Button>
                  </Col>
                  <Col></Col>
                  <Col></Col>
                  <Col>
                    <Button color="success" onClick={(e) => this.vote(e, 'yes')}>In Person</Button>
                  </Col>
                </Row>
              </CardFooter>
            </Card>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default App;

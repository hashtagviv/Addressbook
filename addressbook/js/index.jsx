import React from 'react';
import PropTypes from 'prop-types';
import Address from './address';
class Index extends React.Component {
    constructor(props) {
      super(props);
      this.state = { results: [], url: '', size : 0, next: ''};
      this.fetchData = this.fetchData.bind(this);
      if (performance.type === 2) {
        this.state = history.state;
      }
    }
    componentDidMount() {
      if (performance.type === 2) {
        return;
      }
      fetch(this.props.url, { credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          this.setState({
            results: data.results,
            size :data.size,
            next:data.next,
            hasnext: data.next != '',
          });
        })
        .catch(error => console.log(error)); // eslint-disable-line no-console
    }
    fetchData() {
      fetch(this.state.next, { credentials: 'same-origin' })
        .then(response => response.json())
        .then((data) => {
          this.setState({
            results: data.results,
          });
          history.replaceState(this.state, {});
        })
        .catch(error => console.log(error)); // eslint-disable-line no-console
    }
  
    render() {
      history.replaceState(this.state, {});
      return (
        <div>
            <table id="myTable" class="table table-bordered table-hover table-striped">
                <thead class="thead-dark">
                    <tr class="font-weight-bolder text-monospace">
                        <th>First Name </th>
                        <th>Last Name</th>
                        <th> Company</th>
                        <th> Email </th>
                        <th> Category</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.results.map(item => (
                    <Address url = {item.url} size = {this.state.size} addressid= {item.addressid}/>
                  ))}
                </tbody>
            </table>
        </div>
      );
    }
  }
  
  Index.propTypes = {
    url: PropTypes.string.isRequired,
  };
  
  export default Index;
  
import React from 'react';
import PropTypes from 'prop-types';
import ReactTable from 'react-table';
class Table extends React.Component {
    constructor(props) {
      super(props);
      this.state = { results: [], url: '' };
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
      const columns = [{Header: 'Last Name', accessor: 'lastname'},
                       {Header : 'First Name', accessor: 'firstname'},
                       {Header: 'Company', accessor: 'Company'},
                       {Header : 'Email', accessor : 'Email'},
                       {Header : 'Category', accessor : 'Category'}];
      return (
        <hi> a</hi>
      );
    }
  }
  
  Table.propTypes = {
    url: PropTypes.string.isRequired,
  };
  
  export default Table;
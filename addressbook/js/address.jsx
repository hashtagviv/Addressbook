import React from 'react';
import PropTypes from 'prop-types';

class Address extends React.Component {
    constructor(props) {
      // Initialize mutable state
      super(props);
      this.state = { img_url: '', owner: '', age: 0, owner_show_url: '', 
                owner_img_url: '', post_show_url: '', url: '', lastAddress : false
              };
    }
  
    componentDidMount() {
      // Call REST API to get post data
      fetch(this.props.url, { credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          this.setState({
            category: data.Category,
            company: data.Company,
            email: data.Email,
            firstname: data.firstname,
            lastname: data.lastname,
            url : data.url,
            lastAddress : this.props.size == this.props.addressid,
            addressurl : "/address/".concat(this.props.addressid)
          });
        })
        .catch(error => console.log(error)); // eslint-disable-line no-console
    }
    render() {
        // Render post
        return (
          <tr> 
            <td class="font-weight-bolder text-monospace"><a href={this.state.addressurl}>{this.state.firstname}</a></td>
            <td class="text-monospace font-weight-light">{this.state.lastname}</td>
            <td class="text-monospace font-weight-light">{this.state.company}</td>
            <td class="text-monospace font-weight-light">{this.state.email}</td>
            <td class="text-monospace font-weight-light">{this.state.category}</td>
            {this.state.lastAddress &&
            <td id="lastaddress" class="invisible"></td>}
          </tr>
        );
      }
    }
Address.propTypes = {
    url: PropTypes.string.isRequired,
};
export default Address;
          
import React from 'react';
import ReactDOM from 'react-dom';
import Index from './index';
import setfinished from './../static/js/datatable'
ReactDOM.hydrate(
    <Index url="/api/v1/add"/>,
  document.getElementById('reactEntry'),
);

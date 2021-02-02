import React, { Component } from 'react';
import Worker from "./Worker"
class Workers extends Component {
    state = { }
    render() { 
        return  <React.Fragment>
            {this.props.workers.map(worker =>  <Worker workerStatus={worker.status} workerName={worker.name} workerId={worker.id}/> )}
        </React.Fragment>
    }
}
 
export default Workers;
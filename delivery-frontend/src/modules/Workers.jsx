import React, { Component } from 'react';
import Worker from "./Worker"
class Workers extends Component {
    state = { workers:this.props.workers  }
    render() { 
        return  <React.Fragment>
            {this.state.workers.map(worker =>  <Worker workerStatus= {worker.status} workerName={worker.name} workerId={worker.id}/> )}
        </React.Fragment>
    }
}
 
export default Workers;
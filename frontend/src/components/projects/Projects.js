import React, { Component, Fragment } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getProjects, deleteProject} from "../../actions/projects";

export class Projects extends Component {
    static propTypes = {
        projects: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getProjects();
    }

    render() {
        return (
            <Fragment>
                <h2>Projects</h2>
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th />
                    </tr>
                    </thead>
                    <tbody>
                    {
                        this.props.projects.map(project => (
                             <tr key={project.id}>
                                <td>{project.id}</td>
                                <td>{project.name}</td>
                                <td>
                                    <button
                                        onClick={this.props.deleteProject.bind(this, project.id)}
                                            className="btn btn-danger btn-sm"
                                    >{" "}
                                    Delete
                                    </button>
                                </td>

                                </tr>
                            )

                        )
                    }
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    projects: state.projects.projects
});

export default connect(
    mapStateToProps, { getProjects, deleteProject }
    )(Projects);
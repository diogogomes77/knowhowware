import axios from 'axios';

import { GET_PROJECTS, DELETE_PROJECT} from "./types";

// LIST PROJECTS
export const getProjects = () => dispatch => {
    axios
        .get('/api/projects/')
        .then(res => {
            dispatch({
                type: GET_PROJECTS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};

// DELETE PROJECTS
export const deleteProject = (id) => dispatch => {
    axios
        .get(`/api/projects/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_PROJECT,
                payload: id
            });
        })
        .catch(err => console.log(err));
};
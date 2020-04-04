import { GET_PROJECTS, DELETE_PROJECT } from '../actions/types.js';

const initialState = {
    projects: []
};

export default function(state = initialState, action){
    switch(action.type) {
        case GET_PROJECTS:
            return {
                ...state,
                projects: action.payload
            };
        case DELETE_PROJECT:
            return {
                ...state,
                projects: state.projects.filter(
                    project => project.id !== action.payload
                )
            };
        default:
            return state;
    }
}
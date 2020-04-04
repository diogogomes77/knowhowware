import React, { Fragment} from 'react';
import Form from './Form';
import Projects from './Projects';

export default function Dashboard() {
    return (
            <Fragment>
                <Form />
                <Projects />
            </Fragment>
    )
}

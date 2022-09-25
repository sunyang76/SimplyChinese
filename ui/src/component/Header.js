import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Form from 'react-bootstrap/Form';

function Header() {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <div>
            <Button variant="link" size="sm" onClick={handleShow}>
                Sign up / Login
            </Button>
            <Modal show={show} onHide={handleClose} aria-labelledby="contained-modal-title-vcenter"
                centered>
                <Modal.Body>
                    <Tabs
                        defaultActiveKey="profile"
                        id="uncontrolled-tab-example"
                        className="mb-3">
                        <Tab eventKey="home" title="Sign up">
                            <FloatingLabel
                                controlId="floatingInput"
                                label="Email address"
                                className="mb-3"
                            >
                                <Form.Control type="email" placeholder="name@example.com" />
                            </FloatingLabel>
                            <FloatingLabel controlId="floatingPassword" label="Name">
                                <Form.Control type="text" placeholder="Name" />
                            </FloatingLabel>
                            <div class="row text-right mt-3">
                                <Button variant="primary" onClick={handleClose}>
                                    Sign up
                                </Button>
                            </div>
                        </Tab>
                        <Tab eventKey="profile" title="Log in">
                            <FloatingLabel
                                controlId="floatingInput"
                                label="Email address"
                                className="mb-3"
                            >
                                <Form.Control type="email" placeholder="name@example.com" />
                            </FloatingLabel>
                            <div class="row text-right mt-3">
                                <Button variant="primary" onClick={handleClose}>
                                    Log in
                                </Button>
                            </div>
                        </Tab>
                    </Tabs>


                </Modal.Body>
                {/* <Modal.Footer>

                </Modal.Footer> */}
            </Modal>
        </div>
    )
}

export default Header;
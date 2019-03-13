import React, { Component } from "react";
import {Link} from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"

export default class IndexPage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: this.props.data,
        }
    }

    render() {
        return(
            <Layout>
                <p>Vilka är det mest populära stugorna på Stugknuten.com?</p>
                <ul>
                    <li><Link to="/stugor/goteborg">Göteborg</Link></li>
                    <li><Link to="/stugor/oland">Öland</Link></li>
                </ul>
                <div style={{maxWidth: `300px`, marginBottom: `1.45rem`}}>
                    <Image/>
                </div>
            </Layout>
        );
    }
}

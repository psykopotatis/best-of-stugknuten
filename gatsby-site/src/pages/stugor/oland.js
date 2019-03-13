import React, { Component } from "react";
import {Link} from "gatsby"

import Layout from "../../components/layout"
import Image from "../../components/image"

export default class IndexPage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: this.props.data,
        }
    }

    renderItem(item, index) {
        const total = item.node.engagement.reaction_count + item.node.engagement.comment_count + item.node.engagement.comment_plugin_count + item.node.engagement.share_count;
        return (
            <div className="col-sm-3 mb-4">
                <div className="card" key={item.node.id}>
                    <img src={item.node.image_url} className="card-img-top" alt="Stuga!" />
                    <div className="card-body">
                        <a href={item.node.href} target="_blank">
                            <h5 className="card-title">{item.node.title}</h5></a>
                        <p className="card-text">
                            <i className="fab fa-facebook"></i> {total} likes
                            <br/>
                            {item.node.location}</p>
                    </div>
                </div>
            </div>
        );
    }

    render() {
        return(
            <Layout>
                <h1>Hej!</h1>
                <p>Mest poulära stugor på Öland.</p>
                <div className="row">
                    { this.state.data.allLikesOlandJson.edges.map(this.renderItem) }
                </div>
                <div className="row" style={{maxWidth: `300px`, marginBottom: `1.45rem`}}>
                    <Image/>
                </div>
            </Layout>
        );
    }
}

export const query = graphql`
    query {
        allLikesOlandJson {
            edges {
                node {
                    id
                    title
                    location
                    href
                    image_url
                    engagement {
                        comment_count
                        comment_plugin_count
                        reaction_count
                        share_count
                    }
                }
            }
        }
    }
`;
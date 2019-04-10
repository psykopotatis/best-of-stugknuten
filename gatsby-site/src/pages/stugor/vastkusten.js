import React, { Component } from "react";

import Layout from "../../components/layout"
import Image from "../../components/image"
import Cottage from './../../components/Cottage';


export default class IndexPage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: this.props.data,
        }
    }

    renderItem(item) {
        return (
            <Cottage item={item} />
        );
    }

    render() {
        return(
            <Layout>
                <h1>Hej!</h1>
                <p>Mest poulära stugor på Västkusten.</p>
                <div className="row">
                    { this.state.data.allLikesVastkustenJson.edges.map(this.renderItem) }
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
        allLikesVastkustenJson {
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
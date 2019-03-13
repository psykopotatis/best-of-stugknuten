import React, {Component} from "react";
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

    renderItem(item) {
        return (
            <div key={item.node.id}>
                reaction_count: {item.node.engagement.reaction_count} --
                <a href={item.node.url} target="_blank">{item.node.url}</a>
            </div>
        );
    }

    render() {
        return (
            <Layout>
                <p>Mest poulära stugor i Göteborg.</p>
                {this.state.data.allResultJson.edges.map(this.renderItem)}
                <div style={{maxWidth: `300px`, marginBottom: `1.45rem`}}>
                    <Image/>
                </div>
            </Layout>
        );
    }
}

export const query = graphql`
  query {
      allResultJson {
        edges {
          node {
            id
            url
            engagement {
              comment_count
              reaction_count
              share_count
              comment_plugin_count
            }
          }
        }
      }
    }
`
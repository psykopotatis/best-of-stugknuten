import React, {Component} from "react";
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
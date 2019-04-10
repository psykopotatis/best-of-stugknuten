import React, { Component } from "react";

export default class Cottage extends Component {
    render() {
        const item = this.props.item;
        const total = item.node.engagement.reaction_count + item.node.engagement.comment_count + item.node.engagement.comment_plugin_count + item.node.engagement.share_count;

        return(
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
}
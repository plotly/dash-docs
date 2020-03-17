import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {replace} from 'ramda';
import { History } from '@plotly/dash-component-plugins';


class PageMenu extends Component {
    constructor(props) {
        super(props);
        this.renderLinksInDom = this.renderLinksInDom.bind(this);
    }

    componentDidUpdate() {
        this.renderLinksInDom();
    }

    componentDidMount() {
        this.renderLinksInDom();
    }

    renderLinksInDom() {
        const parent = document.getElementById('page-menu--links');
        const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        const ignoreElementsNodeList = document.querySelectorAll(`
            .example-container h1,
            .example-container h2,
            .example-container h3,
            .example-container h4,
            .example-container h5,
            .example-container h6
        `);
        const ignoreElementsArray = [];
        for(let i=0; i<ignoreElementsNodeList.length; i++) {
            ignoreElementsArray[i] = ignoreElementsNodeList[i];
        }

        const links = [];
        for(let i=0; i<elements.length; i++) {
            const el = elements[i];
            if(ignoreElementsArray.indexOf(el) > -1) {
                continue;
            }
            if (!el.id) {
                el.id = `${replace(/ /g, '-', el.innerText).toLowerCase()}`;
            }
            /*
             * TODO - Replace with a proper a and remove pageMenuScroll
             * once https://github.com/plotly/dash-core-components/issues/769
             * is fixed
             */
            links.push(`
                <div class="page-menu--link-parent">
                    <span class="page-menu--link" onClick="pageMenuScroll('${el.id}')">
                        ${el.innerText}
                    </span>
                </div>
            `);
        };
        parent.innerHTML = links.join('');
    }

    render() {
        const {id, loading_state} = this.props;
        return (
            <div
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
                id={id}
                className='page-menu'
            >
                <div className='page-menu--header'>{'On This Page'}</div>
                <div id="page-menu--links"/>
            </div>
        )
    }
}

PageMenu.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /*
     * dummy props to force updates
     */
    dummy: PropTypes.string,
    dummy2: PropTypes.string,

    /**
     * Object that holds the loading state object coming from dash-renderer
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default PageMenu;
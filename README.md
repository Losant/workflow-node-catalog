# Losant Node Catalog
This repository contains a collection of contributed nodes for [Losant's Visual Workflow Engine](https://docs.losant.com/workflows/overview/). These nodes provide additional capabilities and third-party integrations above and beyond the built-in nodes provided by the Losant workflow editor.

## Importing a Contributed Node
Each folder in this repository is made up of one or more `.node` files. Each file represents a self-contained node that can be imported into your Losant Application as a [Custom Node](https://docs.losant.com/workflows/custom-nodes/overview/).

First, download the `.node` file that you'd like to import to your local computer. Next, navigate to your application's Custom Nodes page by using the `Workflows -> Custom Nodes` main application menu. Lastly, import the node using the `Import` button that's located at the top-right of the Custom Node list. This will prompt you to upload the `.node` file you previously downloaded.

Once the Contributed Node is imported, it will immediately be available in the `Custom Nodes` section in your workflow palette.

## Adding a Node to this Catalog
Contributing nodes to this catalog is an excellent way to expose your product or service to the Losant developer community.

### 1. Build and Test the Node

The first step to contributing a node is to following the custom node [documentation](https://docs.losant.com/workflows/custom-nodes/overview/) and [walkthrough](https://docs.losant.com/workflows/custom-nodes/walkthrough/) to develop your new node within your own Losant application. The existing nodes in this catalog provide great reference examples.

### 2. Version the Node

When you're ready to submit the node, [create a version](https://docs.losant.com/workflows/custom-nodes/overview/#versioning) of the node using [Semantic Versioning](https://semver.org/). Following Semantic Versioning is a requirement for all contributed nodes. This allows the consumers of these nodes to better understand the impact of each new revision.

### 3. Export the Node

Using Losant's built-in export feature, export the node to a `.node` file. The name of the `.node` file should be the same as your custom node's name with spaces replaced with dashes. For example, if your node's name is "Moving Average", the exported file should be named `moving-average.node`.

### 4. Submit Pull Request
Contributing nodes to this catalog is performed by submitting a pull request against the `master` branch of this repository. Each contribution will be reviewed by the Losant team.

If you are contributing a single node, add a new folder with the name of the node. If your contribution is made up of several nodes, which is common for integrations with third-party services or APIs, name the folder after the service or product. Each folder can contain multiple `.node` files.

If at all possible, try to keep each node self-contained, which means they do not depend on other contributed nodes for their functionality.

Add a `README.md` file to your folder with instructions on how to properly consume your contributed node. Refer to the nodes in this repository for example readme files.

Add a `LICENSE` file to your folder with your specific licensing terms. Losant prefers the [MIT License](https://opensource.org/licenses/MIT) where applicable.

---

Copyright © 2018 Losant IoT, Inc

https://www.losant.com

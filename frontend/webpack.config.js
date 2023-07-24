const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "/dist"),
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        })
    ]
}

// import SwaggerUI from 'swagger-ui'
// import 'swagger-ui/dist/swagger-ui.css';

// const spec = require('./swagger-config.yaml');

// const ui = SwaggerUI({
//   spec,
//   dom_id: '#swagger',
// });

// ui.initOAuth({
//   appName: "Swagger UI Webpack Demo",
//   clientId: 'implicit'
// });
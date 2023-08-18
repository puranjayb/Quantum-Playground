import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "flowbite"


import "./index.css";
import App from './App'
import Layout from "./hoas/Layout";
import Predict from "./pages/Predict";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout>
      <App />
    </Layout>,
  },
  {
    path: "/about",
    element: <div>About</div>,
  },
  {
    path: "/predict",
    element: <Layout>
      <Predict />
      </Layout>,
  }
]);


ReactDOM.createRoot(document.getElementById('root')!).render(
<RouterProvider router={router} />
);
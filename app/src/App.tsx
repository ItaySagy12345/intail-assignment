import defaultRouter from "./routes/router";

import { RouterProvider } from "react-router-dom";

function App() {
  return <RouterProvider router={defaultRouter} />;
}

export default App;

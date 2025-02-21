import { RouterProvider } from "react-router-dom";
import defaultRouter from "./routes/router";

function App() {
  return (
    <RouterProvider router={defaultRouter} />
  );
}

export default App;

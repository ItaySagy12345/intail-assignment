import { Routes } from "generics/enums/routes-enums";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function HomePage() {
  const navigate = useNavigate();

  useEffect(() => {
    navigate(`/${Routes.QUOTES}`);
  }, []);

  return (<></>);
}
export default HomePage;
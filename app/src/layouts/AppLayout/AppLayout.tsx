import Logo from "components/Logo/Logo";
import { Outlet } from 'react-router-dom';

function AppLayout() {
  return (
    <>
      <Logo />
      <Outlet />
    </>
  );
}

export default AppLayout;
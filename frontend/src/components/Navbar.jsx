import { Link, useNavigate } from "react-router-dom";
import { logoutUser, isAuthenticated } from "../services/auth";

function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logoutUser();
    navigate("/login");
  };

  return (
    <nav className="flex justify-between p-4 bg-gray-900 text-white">
      <div className="flex gap-4">
        <Link to="/">Home</Link>
        {isAuthenticated() && <Link to="/dashboard">Dashboard</Link>}
      </div>

      {isAuthenticated() ? (
        <button onClick={handleLogout} className="bg-red-500 px-3 py-1 rounded">
          Logout
        </button>
      ) : (
        <Link to="/login">Login</Link>
      )}
    </nav>
  );
}

export default Navbar;
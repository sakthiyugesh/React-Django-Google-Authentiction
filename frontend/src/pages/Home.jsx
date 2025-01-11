import React, { useContext } from "react";
import AuthContext from "../auth/AuthContext";

const Home = () => {
  const { user, logoutUser } = useContext(AuthContext);
  return (
    <>
      <div>
        {!user ? (
          <div>
            {" "}
            <h2>No User Found..!</h2>
            <a href="login">Go to Login..</a>
          </div>
        ) : (
          <div>
            <h2>
              Hey <i>{user.first_name}!</i>
            </h2>
            <p>Email: {user.email}</p>
            <button onClick={logoutUser}>Logout</button>
          </div>
        )}
      </div>
    </>
  );
};

export default Home;

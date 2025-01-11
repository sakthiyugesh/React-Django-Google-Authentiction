import React, { useContext, useEffect } from "react";
import AuthContext from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";
import GoogleLoginButton from "../components/GoogleLoginButton";

const Login = () => {
  const { user } = useContext(AuthContext);

  return (
    <div>
      {!user ? (
        <div>
          <GoogleLoginButton />
        </div>
      ) : (
        <p>Redirecting to home...</p>
      )}
    </div>
  );
};

export default Login;

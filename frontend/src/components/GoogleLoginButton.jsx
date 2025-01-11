// GoogleLoginButton.js

import { useGoogleLogin } from "@react-oauth/google";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const GoogleLoginButton = () => {
  const navigate = useNavigate();
  const login = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      const { access_token } = tokenResponse;
      const response = await axios.post(
        "http://localhost:8000/social_auth/auth/google/",
        { token: access_token }
      );
      // Handle JWT tokens here (store in localStorage, etc.)
      localStorage.setItem("authTokens", JSON.stringify(response.data));
      navigate("/");
      window.location.reload();
    },
    onError: (error) => {
      console.error("Login Failed:", error);
    },
  });

  return <button onClick={login}>Sign in with Google</button>;
};

export default GoogleLoginButton;

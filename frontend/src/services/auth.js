export const loginUser = async (username, password) => {
  try {
    const res = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await res.json();

    if (!res.ok) {
      return { success: false, message: data.message };
    }

    localStorage.setItem("token", data.token);
    localStorage.setItem("user", username);

    return { success: true };
  } catch (err) {
    return { success: false, message: "Server error" };
  }
};
export const getDashboardData = async () => {
  const token = localStorage.getItem("token");

  const res = await fetch("http://localhost:5000/dashboard-data", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
  });

  const data = await res.json();
  return data;
};
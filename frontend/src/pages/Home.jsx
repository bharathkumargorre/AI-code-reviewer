function Home() {
  const user = localStorage.getItem("user");

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-50 to-purple-100">
      <h1 className="text-4xl font-bold mb-3">
        Welcome {user || "Guest"} 🚀
      </h1>

      <p className="text-gray-600">
        Your React SaaS app is running successfully
      </p>
    </div>
  );
}

export default Home;
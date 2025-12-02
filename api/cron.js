import { spawn } from "child_process";

export default function handler(req, res) {
  const python = spawn("python3", ["api/script.py"]);

  python.stdout.on("data", (data) => console.log("[PYTHON]:", data.toString()));
  python.stderr.on("data", (data) => console.error("[ERROR]:", data.toString()));

  python.on("close", () => {
    res.status(200).json({
      status: "Cron executed successfully",
      timestamp: new Date().toISOString(),
    });
  });
}
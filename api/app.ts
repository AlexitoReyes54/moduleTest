import { file } from "bun";
import watchesData from "./db.json" with { type: "json" };
import type { Watch } from "./types";

// Type assertion ensuring the imported data matches the interface
const watches: Watch[] = watchesData;

const PORT = Number(process.env.PORT) || 8100;

Bun.serve({
	port: PORT,
	async fetch(req) {
		const url = new URL(req.url);

		// 1. Serve the HTML file
		if (url.pathname === "/") {
			return new Response(file("index.html"));
		}

		// 2. JSON Endpoint 1
		if (url.pathname === "/api/status" && req.method === "GET") {
			return Response.json({ status: "running", code: 200 });
		}

		// 3. JSON Endpoint 2 - Serves the exact db.json array untouched
		if (url.pathname === "/api/data" && req.method === "GET") {
			return Response.json(watches);
		}

		// Fallback 404 for unknown routes
		return new Response("Not Found", { status: 404 });
	},
});

console.log(`Server running at http://localhost:${PORT}`);

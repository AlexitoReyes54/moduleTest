import { file } from "bun";
import watchesData from "./db.json" with { type: "json" };
import type { Watch } from "./types";

// Type assertion ensuring the imported data matches the interface
const watches: Watch[] = watchesData;

const PORT = Number(process.env.PORT) || 8100;
const corsHeaders = {
	"Access-Control-Allow-Origin": "*", // Change to "http://localhost:3000" or similar to restrict
	"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
	"Access-Control-Allow-Headers": "Content-Type, Authorization",
};

Bun.serve({
	port: PORT,
	async fetch(req) {
		const url = new URL(req.url);

		// 1. Handle preflight OPTIONS request
		if (req.method === "OPTIONS") {
			return new Response(null, {
				status: 204,
				headers: corsHeaders,
			});
		}

		// Helper function to attach CORS headers to any Response
		const withCors = (res: Response) => {
			Object.entries(corsHeaders).forEach(([key, value]) => {
				res.headers.set(key, value);
			});
			return res;
		};

		// 2. Serve the HTML file
		if (url.pathname === "/") {
			return withCors(new Response(file("index.html")));
		}

		// 3. JSON Endpoint 1
		if (url.pathname === "/api/status" && req.method === "GET") {
			return withCors(Response.json({ status: "running", code: 200 }));
		}

		// 4. JSON Endpoint 2 - Serves the exact db.json array untouched
		if (url.pathname === "/api/data" && req.method === "GET") {
			return withCors(Response.json(watches));
		}

		// Fallback 404 for unknown routes
		return withCors(new Response("Not Found", { status: 404 }));
		
	},
});

console.log(`Server running at http://localhost:${PORT}`);

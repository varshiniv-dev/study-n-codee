const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let width = window.innerWidth;
let height = window.innerHeight;

canvas.width = width;
canvas.height = height;

window.addEventListener("resize", () => {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
});

// ---- cursor / center ----
let targetX = width / 2;
let targetY = height / 2;

let centerX = targetX;
let centerY = targetY;

window.addEventListener("pointermove", (e) => {
    const rect = canvas.getBoundingClientRect();
    targetX = e.clientX - rect.left;
    targetY = e.clientY - rect.top;
});

// ---- many arms coming out from the center ----
const ARMS = 60; // number of lines
const arms = [];

for (let i = 0; i < ARMS; i++) {
    const angle = (i / ARMS) * Math.PI * 2;
    const radius = 15 + Math.random() * 120;

    arms.push({
        baseAngle: angle,
        angle: angle,
        radius: radius,
        x: centerX + Math.cos(angle) * radius,
        y: centerY + Math.sin(angle) * radius,
        vx: 0,
        vy: 0,
    });
}

// ---- tiny stars in the background ----
const STARS = 140;
const stars = [];

for (let i = 0; i < STARS; i++) {
    stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.3 + 0.3,
        twinkle: Math.random() * 0.05 + 0.02,
        phase: Math.random() * Math.PI * 2,
    });
}

function drawStars() {
    for (const s of stars) {
        s.phase += s.twinkle;
        const alpha = 0.3 + 0.4 * (0.5 + 0.5 * Math.sin(s.phase));

        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255,255,255,${alpha})`;
        ctx.fill();
    }
}

// ---- animation loop ----
function loop() {
    // soft fade
    ctx.fillStyle = "rgba(0, 0, 0, 0.32)";
    ctx.fillRect(0, 0, width, height);

    drawStars();

    // move center smoothly towards cursor
    centerX += (targetX - centerX) * 0.12;
    centerY += (targetY - centerY) * 0.12;

    ctx.save();
    ctx.lineCap = "round";
    ctx.lineJoin = "round";

    // glow settings
    ctx.shadowColor = "#ffffff";
    ctx.shadowBlur = 18;

    // draw all arms
    for (const arm of arms) {
        // make each arm wiggle a bit so it doesn't look rigid
        arm.angle += (Math.random() - 0.5) * 0.03;

        const targetArmX =
            centerX + Math.cos(arm.angle) * arm.radius;
        const targetArmY =
            centerY + Math.sin(arm.angle) * arm.radius;

        // spring motion towards its target
        arm.vx += (targetArmX - arm.x) * 0.12;
        arm.vy += (targetArmY - arm.y) * 0.12;

        // softness
        arm.vx *= 0.82;
        arm.vy *= 0.82;

        arm.x += arm.vx;
        arm.y += arm.vy;

        // thickness: thicker near the center, thinner outside
        const dx = arm.x - centerX;
        const dy = arm.y - centerY;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const t = Math.min(dist / 160, 1); // 0 -> near center, 1 -> far
        const lineWidth = 4 * (1 - t) + 0.8; // from 8px to 1px

        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(arm.x, arm.y);

        ctx.lineWidth = lineWidth;
        ctx.strokeStyle = "rgba(255,255,255,0.95)";
        ctx.stroke();
    }

    ctx.restore();

    // bright core in the middle (not scary, just pretty glow)
    ctx.beginPath();
    ctx.arc(centerX, centerY, 4, 0, Math.PI * 2);
    ctx.fillStyle = "#ffffff";
    ctx.shadowColor = "#ffffff";
    ctx.shadowBlur = 30;
    ctx.fill();
    ctx.shadowBlur = 0;

    requestAnimationFrame(loop);
}

loop();
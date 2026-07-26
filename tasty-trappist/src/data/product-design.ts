export const productDesignProjects = [
  {
    id: "1.1",
    slug: "tofu-hardness-analyzer",
    title: "Tofu Hardness Analyzer",
    description: "Desktop hardness-measurement device built from a salvaged 3D printer, using computer vision and a load cell to grade tofu.",
    tags: "Mechatronics · Computer Vision · ESP32",
  },
  {
    id: "1.2",
    slug: "monitor-stand",
    title: "Monitor Stand",
    description: "Monitor desk stand with parametric sizing.",
    tags: "Mechanical Design · SolidWorks · Technical Details",
  },
  {
    id: "1.3",
    slug: "pipe-lights",
    title: "Pipe Lights",
    description: "Industrial pipe-style lighting fixture.",
    tags: "Product Design",
  },
  {
    id: "1.4",
    slug: "craftsman-drawer-divider",
    title: "Craftsman Drawer Divider Family",
    description: "Modular drawer organization system with parametric sizing.",
    tags: "Parametric Design · 3D Printing · Manufacturing",
  },
  {
    id: "1.5",
    slug: "home-workshop",
    title: "Home Workshop",
    description: "Custom apartment workshop build.",
    tags: "Furniture Design · Workshop · Final Product",
  },
  {
    id: "1.6",
    slug: "ivy-pot",
    title: "Ivy Pot",
    description: "Decorative planter with integrated climbing support.",
    tags: "Product Design · 3D Printing · Final Product",
  },
  {
    id: "1.7",
    slug: "light-bulb-recycle",
    title: "Light Bulb Recycle",
    description: "Small lamp using a recycled light bulb as a diffuser.",
    tags: "Electronics · 3D Printing · Product Design",
  },
  {
    id: "1.8",
    slug: "egg-jig",
    title: "Egg Jig",
    description: "Conveyor egg-handling jig with controlled clamping and passive actuation.",
    tags: "Mechanical Design · Product Design · Automation",
  },
  {
    id: "1.9",
    slug: "home-bar",
    title: "Home Bar",
    description: "Handbuilt home bar.",
    tags: "Woodworking · Furniture Design · Final Product",
  },
] as const;

export type ProductDesignProject = (typeof productDesignProjects)[number];

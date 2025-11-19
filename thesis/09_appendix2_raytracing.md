---
title: "Appendix 2: Ray Tracing For Enhanced Visualization In DEM"
tags: [thesis, appendix-2, ray-tracing, visualization, rendering, computer-graphics]
aliases: [Appendix 2, Ray Tracing, DEM Visualization]
---

# Appendix 2 Ray Tracing for Enhanced Visualization in DEM

In Appendix 1, we explored the use of GPUs for general-purpose high-performance computing (GPGPU), leveraging their massively parallel architecture for DEM simulations. While modern GPUs are widely recognized for accelerating scientific computing, their origins lie in a fundamentally different domain: visual rendering. GPUs were initially designed to handle graphics-intensive tasks such as image rendering, shading, and texture mapping. These tasks required the calculation of pixel colors across millions of pixels in real-time, a process naturally suited to parallel computation.

Among the many techniques developed for visual rendering, ray tracing emerged as one of the most powerful methods for producing highly realistic images. Ray tracing simulates the behavior of light in the real world by tracing the paths of rays from a virtual camera through a viewport and into a 3D scene. When these rays intersect with objects, the interactions---such as reflections, refractions, and shading---are computed to determine the final color of each pixel.

This parallelism aligns with the requirements of DEM, where particle interactions can similarly be computed independently. The adoption of GPUs in general computing thus stems from their ability to handle high-dimensional, parallelizable problems across diverse domains, from scientific simulations to image rendering. This chapter explores the application of ray tracing in DEM visualization, covering its fundamental principles and implementation. By integrating ray tracing into DEM studies, we aim to enhance the interpretability and communicability of complex granular behaviors, bridging the gap between computation and visual analysis.

## A2.1. Fundamentals of ray tracing

Ray tracing is a rendering technique that models the interaction of light with objects in a virtual scene, producing images with exceptional realism. At its core, the process involves calculating the path of rays from a virtual camera through a viewport into a 3D scene, determining how these rays interact with objects, and ultimately assigning colors to the pixels they represent. This section introduces key concepts such as the camera, viewport, and the computational pipeline of ray tracing.

### A2.1.1. Camera, ray, viewport, and scene

![](thesis/assets/media/image166.png)

Fig. A2.1. Ray tracing workflow: Rays originate from the camera, pass through the viewport, and interact with objects in the 3D scene, determining the color information for each pixel.

The camera in ray tracing acts as the observer\'s eye, defining the origin of rays and their direction. It is characterized by parameters such as position, orientation, and field of view. The viewport represents the screen or image plane onto which the scene is projected. Each pixel on the viewport corresponds to a ray that originates from the camera and passes through that pixel's location in the scene.

The goal of ray tracing is to calculate the color (RGB values) of each pixel on the viewport by simulating the interaction of its corresponding ray with objects in the scene. This requires solving the fundamental problem of determining where and how each ray intersects with objects.

Fig. A2.1 illustrates the basic workflow of ray tracing, where rays originate from the camera, pass through the viewport, and interact with objects in the 3D scene. The resulting interactions determine the color information for each pixel on the viewport.

### A2.1.2. Determining pixel colors: ray-object intersection

The ray tracing process begins by iterating over every pixel in the viewport, generating a primary ray for each. These rays are traced into the 3D scene to identify intersections with objects. For each intersection, additional calculations are performed to evaluate lighting, material properties, and other effects such as shadows or reflections. If a ray intersects with an object, the nearest intersection point is determined. The object\'s material properties, combined with lighting conditions, are then used to compute the pixel\'s final color. Rays that do not intersect with any object are typically assigned a background color, representing the environment or sky. To visualize the setup, Fig. A2.2 presents two spheres rendered with refined, elegant colors---muted green (RGB: 0.45, 0.55, 0.47) and muted violet (RGB: 0.35, 0.30, 0.37).

![](thesis/assets/media/image167.png)

Fig. A2.2. Rendered spheres with purple and green colors

## A2.2. Lighting models in ray tracing

In ray tracing, lighting models play a critical role in determining the appearance of objects in a rendered scene. The interplay between light sources and object surfaces determines the final pixel color, achieved by applying illumination coefficients to the object\'s base color. This section introduces three fundamental types of light sources commonly employed in rendering: ambient light, point light, and directional light.

### A2.2.1. Ambient Light

Ambient light represents a constant, uniform light source present throughout the scene, simulating indirect lighting from all directions. Unlike other light types, ambient light does not originate from a specific location. Instead, it provides a baseline illumination to ensure that surfaces not directly exposed to light sources are still visible. The contribution of ambient light to the object's color is determined by an ambient coefficient, typically a small value (e.g., 0.1 or 0.2). Mathematically, the ambient lighting contribution​ is given by:

$I_{a} = C \bullet k_{a}$ (A2-1)

where $C$ is the object's base color, and $k_{a}$ is the ambient coefficient.

### A2.2.2. Point light

Point lights represent localized sources of light that radiate uniformly in all directions from a specific position. They mimic real-world light sources like bulbs or candles. The intensity of light decreases with distance from the source, modeled by an attenuation factor.

![](thesis/assets/media/image168.png)

Fig. A2.3. Diffuse reflection of light, showing the relationship between the light direction, surface normal, and reflection distribution

![](thesis/assets/media/image169.png)

Fig. A2.4. Specular reflection, illustrating the relationship between the light ray, surface normal, and viewer position

For point light, the diffuse and specular contributions depend on the light direction, surface normal, and viewer position. Diffuse lighting is proportional to the cosine of the angle between the light direction vector $L$ and the surface normal $N$, as illustrated in Fig. A2.3. Specular lighting depends on the angle between the reflected light vector　$R$ and the viewer direction $V$, as shown in Fig. A2.4.

The intensity $I_{p}$ at a point is computed as:

$I_{p} = C \cdot (k_{d}\left( \mathbf{L} \cdot \mathbf{N} \right) + k_{s}\left( \mathbf{R} \cdot \mathbf{V} \right)^{n})$ (A2-2)

, where $k_{d}$ and $k_{s}$ ​are diffuse and specular coefficients,$n$ is the shininess factor.

### A2.2.3. Directional light

Directional light represents a distant light source, such as sunlight, where the light rays are considered parallel. Unlike point lights, directional light does not attenuate with distance. The illumination model for directional light is similar to that of point light but simplifies calculations as the light direction remains constant for the entire scene.

![](thesis/assets/media/image170.png)

Fig. A2.5. Rendering of two spheres under directional light showcasing diffuse and specular reflections.

The interaction of objects with light sources, combining ambient, diffuse, and specular reflections, is demonstrated in Fig. A2.5. This figure depicts two spheres illuminated with ambient light, directional light, and specular reflections, where the lighting highlights the material properties.

## A2.3. Reflection and refraction between objects

Previous sections focused on light interactions with individual objects, such as diffuse and specular reflections influenced by various light sources. However, these computations only accounted for direct lighting effects and did not include interactions between objects within the scene. To realistically simulate the intricate interplay of light, it becomes necessary to account for reflections and refractions between objects, which are essential for capturing phenomena such as mirrored surfaces and transparent materials.

This process is achieved through recursive ray tracing. When a ray intersects an object, secondary rays are spawned to model light interactions with other objects in the environment.

### A2.3.1. Reflection 

Reflections are crucial to creating realistic scenes in ray tracing, as they simulate how light bounces off surfaces and interacts with other objects in the environment. When a light ray strikes a reflective surface, part of its energy is reflected. The direction of the reflected ray is determined by the surface normal and the incident ray according to the law of reflection.

In the ray tracing process, reflections are computed by generating a secondary ray at the point of intersection between the primary ray and the reflective surface. This reflected ray continues to propagate through the scene, checking for further intersections with other objects. Each subsequent intersection contributes to the pixel's final color by considering the material properties and lighting conditions at each reflection point. This iterative process allows for the simulation of mirrored surfaces and multi-object reflections.

![](thesis/assets/media/image171.png)

Fig. A2.6. Illustration of inter-object reflection showing ray paths

Fig. A2.6 illustrates how a light ray interacts with a reflective surface. The incident ray strikes the surface of one object, and the reflected ray intersects with a second object. The color and lighting contributions from the second object are then calculated and combined with those of the first to produce the final reflected effect. The reflection is computed using Eq. (A2-3):

$\mathbf{r} = \mathbf{i} - 2(\mathbf{i} \cdot \mathbf{N})\mathbf{N}$ (A2-3)

, where $\mathbf{r}$ is the reflected ray direction, $\mathbf{i}$ is the incident ray direction, and $\mathbf{N}$ is the normal vector at the point of intersection.

In Fig. A2.7, the visual results of reflections are demonstrated. Both spheres possess reflective properties, but their reflectivity coefficients differ. The sphere on the right exhibits a higher reflectivity, creating a pronounced mirror-like appearance that reflects the checkerboard floor and adjacent sphere. In contrast, the left sphere, with a lower reflectivity coefficient, produces a subtler reflection.

![](thesis/assets/media/image172.png)

Fig. A2.7. Spheres with high (right) and low (left) reflectivity

To prevent infinite recursion in complex scenes, a recursion depth is typically set. This parameter defines the maximum number of times a ray can reflect before being terminated. By limiting recursion depth, computational resources are managed efficiently while maintaining realistic results.

### A2.3.2. Refraction

In addition to reflection, ray tracing also accounts for refraction, where rays pass through transparent or semi-transparent objects, altering their trajectory according to Snell\'s law. Refraction is calculated using the indices of refraction of the two media involved. Fig. A2.8, illustrates this process, where a ray transitions from the purple object into the green object, resulting in a refracted direction.

![](thesis/assets/media/image173.png)

Fig. A2.8. Refraction of a ray between two objects

Snell\'s law is applied to compute the refracted ray direction:

$\frac{\sin\left( \theta_{i} \right)}{\sin\left( \theta_{refract} \right)} = \frac{n_{2}}{n_{1}}$ (A2-4)

, where $\theta_{i}$ is the angle of incidence, $\theta_{refract}$ is the angle of refraction, and $n_{1}$ and $n_{2}$ are the indices of the refraction for the two media. The refracted ray can further interact with other objects in the scene, contributing to the final color and transparency effects.

![](thesis/assets/media/image174.png)

Fig. A2.9. Combined effects of reflection and refraction on two spheres

This rendered image shown in Fig. A2.9 demonstrates the simultaneous application of reflection and refraction in ray tracing. The sphere on the left primarily showcases refraction, with rays bending as they pass through the transparent surface, distorting the checkerboard pattern behind it. The sphere on the right exhibits reflective properties, with the surrounding environment and nearby objects mirrored on its surface.

## A2.4. Techniques for enhancing quality and efficiency

### A2.4.1. Supersampling and anti-aliasing

Supersampling is a fundamental technique to mitigate aliasing, a common artifact in computer graphics where jagged edges appear along diagonal or curved boundaries due to insufficient sampling resolution. By subdividing each pixel into multiple subpixels, rays are cast through each subpixel to calculate individual color contributions, which are then averaged to determine the final pixel color. This process ensures smoother transitions and more visually appealing results.

![](thesis/assets/media/image175.png)

Fig. A2.10. Supersampled render with 64 samples per pixel, illustrating significant quality improvement and reduced aliasing

In Fig. A2.10, supersampling with 64 samples per pixel is compared to Fig. A2.9, which lacks supersampling. The difference is striking: the jagged edges on the spherical surfaces and the ground plane in Fig. A2.9 are significantly reduced in Fig. A2.10, demonstrating the effectiveness of this technique in enhancing render quality.

Furthermore, anti-aliasing filters, such as box or Gaussian filters, can be applied to further refine the results by blending the subpixel colors, achieving seamless transitions across edges and gradients. While supersampling incurs additional computational cost, its impact on the final render quality makes it indispensable for high-quality visualizations.

### A2.4.2. Spatial partitioning for efficiency

Rendering complex scenes with numerous objects involves a significant computational challenge, particularly when calculating intersections for ray tracing, reflections, and refractions. Without optimization, every ray must be tested against all objects in the scene, leading to a prohibitive computational cost as the scene\'s complexity grows. Spatial partitioning techniques provide an effective solution by organizing objects into a hierarchical or grid-based structure, thereby reducing the number of intersection tests required.

Borrowing concepts from the neighbor search technique introduced in Appendix 1, spatial partitioning in rendering can be enhanced using structures like uniform grids， octrees, or bounding volume hierarchies (BVH). Each of these methods optimizes ray-object interactions by focusing computational effort on relevant regions of the scene.

In uniform grid-based spatial partitioning, the scene is divided into evenly spaced cells. As a ray propagates through the scene, it interacts with all the cells it traverses. Within each cell, only the objects present in that cell are considered for intersection tests. This approach minimizes unnecessary calculations and focuses computational resources on objects the ray is likely to encounter. While straightforward to implement, uniform grids are best suited for scenes with evenly distributed objects and can be less efficient in handling sparse or clustered object distributions.

Octrees divide the scene into a recursive hierarchy of eight cubic regions. Each node of the octree represents a spatial partition, which is further subdivided if it contains multiple objects. Rays only interact with objects in the partitions they traverse, significantly reducing the number of unnecessary intersection tests.

BVH is a hierarchical tree structure designed to optimize ray-object intersection tests by organizing objects into nested bounding volumes. Each node in the BVH represents a bounding volume, which completely encloses either individual objects (leaf nodes) or smaller bounding volumes (internal nodes). While uniform grids divide the space into fixed cells and octrees adaptively refine the space, BVH organizes objects based on their bounding volumes. This dynamic adaptability makes BVH especially effective in scenes with uneven object distributions.

Fig. A2.11 demonstrates the capability of ray tracing to handle scenes with many objects efficiently. Each sphere in this dense granular assembly is rendered with accurate lighting effects, such as reflections and refractions, showcasing the robustness of ray tracing algorithms in managing complex object interactions. The rendering highlights the application of spatial data structures, such as Bounding Volume Hierarchies (BVH) or uniform grids, to optimize the computational workload and achieve high-quality visualizations even for scenes with thousands of objects.

![](thesis/assets/media/image176.png)

Fig. A2.11. Large-scale ray tracing of granular assemblies with accurate reflections

## A2.5. Summary 

Appendix 2 explores the application of ray tracing for enhanced visualization in DEM simulations, showcasing its potential to improve the interpretability of granular material behavior.

Through successive sections, the chapter delves into lighting models, reflection, and refraction, illustrating how these factors are incorporated into ray tracing to achieve photorealistic renderings. The integration of diffuse and specular reflections, coupled with the recursive tracing of rays for inter-object interactions, demonstrates the intricate interplay of physics and computation in creating realistic visuals. This is exemplified through various figures, showcasing improvements in rendering quality with techniques like anti-aliasing.

Efficiency and scalability are addressed through spatial partitioning methods such as uniform grids, octrees, and bounding volume hierarchies, enabling ray tracing to handle complex DEM datasets with many objects. These techniques enhance the capability to visualize highly detailed granular assemblies.

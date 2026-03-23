export const technicalLeadershipProjects = [
	{
		id: '3.1',
		slug: 'automated-fencing-dummy',
		title: 'Automated Fencing Dummy',
		subtitle: 'Mechanical fencing training device — from stalled project to A+',
		tags: 'Concept Design · Mechanism · Team Leadership',
	},
	{
		id: '3.2',
		slug: 'makerspace-operations-overhaul',
		title: 'Makerspace Operations Overhaul',
		subtitle: '12-page improvement proposal — written without being asked',
		tags: 'Self-Initiated · Process Improvement · 5S',
	},
] as const;

export type TechnicalLeadershipProject = (typeof technicalLeadershipProjects)[number];

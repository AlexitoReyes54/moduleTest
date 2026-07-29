export interface WatchCase {
	material: string;
	bezel: string;
	glass: string;
	back: string;
	shape: string;
	diameter: string;
	height: string;
	waterResistance: string;
}

export interface WatchDial {
	color: string;
	material: string;
	indexes: string;
	hands: string;
}

export interface Watch {
	url: string;
	brand: string;
	family: string;
	reference: string;
	name: string;
	movement: string;
	produced: string;
	limited: string;
	case: WatchCase;
	dial: WatchDial;
	mainImage: string;
	gallery: string[];
	description: string;
}

import itasca as it
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
matplotlib.use("Agg")
import matplotlib.colors
import matplotlib.pyplot as plt
from scipy import special
import csv

class DistGetter():
    """
    a distribution of contact direction
     in the assembly of particles
    """
    def __init__(self):
        self.file_n = "contact_dist/distContacts.csv"
        self.file_nMech = "contact_dist/distContactsMech.csv"
        self.skt_file_n = "skeletonData.csv"
        self.skt_file_nMech = "skeletonDataMech.csv"

    def get_ave_force(self):
        "getting avrage force of all the contacts"
        num_c = 0
        con_force = 0.0
        for contact in it.contact.list():
            if contact.__class__ == it.BallBallContact:
                force_vec = np.array(contact.force_global())
                force = np.linalg.norm(force_vec)
                con_force += force
                num_c += 1
            else:
                pass
        ave_force = con_force / num_c
        self.ave_force = ave_force

    def get_data_num(self):
        "getting data from the contact list"
        self.dataArr = np.zeros([self.number_u, self.number_v])
        self.fabTen = np.zeros(shape=(3, 3))
        self.anisoFabTen = np.zeros(shape=(3, 3))

        c_list = it.contact.list()
        c_count = 0
        for contact in c_list:
            # only contacts between particles are counted
            if contact.__class__ == it.BallBallContact:
                c_count += 1

                direction_vec = np.array(contact.normal())
                vec_x = direction_vec[0]
                vec_y = direction_vec[1]
                vec_z = direction_vec[2]
                pos_x = contact.pos_x()
                pos_y = contact.pos_y()
                vec_pos_x = -pos_x/np.sqrt(pos_x**2 + pos_y**2)
                vec_pos_y = -pos_y/np.sqrt(pos_x**2 + pos_y**2)
                vec_rad = (vec_pos_x*vec_x + vec_pos_y*vec_y)
                
                vec_cir = (vec_pos_y*vec_x - vec_pos_x*vec_y)

                vec_x = vec_cir
                vec_y = vec_rad
                vec = np.array([vec_x, vec_y, vec_z])
                for row in np.arange(3):
                    for col in np.arange(3):
                        self.fabTen[row, col] += vec[row] * vec[col]

                if (vec_x == 0.0) and (vec_y == 0.0):
                    self.dataArr[:,0] += 1.0 / self.number_u
                    self.dataArr[:,-1] += 1.0 /self.number_u
                # here divide one contact to several 1/number to avoid
                # valueException 'divided by zero' in cos(u)-calculation
                else:
                    u_con_cosu = vec_x / \
                    np.sqrt(vec_x**2 + vec_y**2)
                    u_con_sinu = vec_y / \
                    np.sqrt(vec_x**2 + vec_y**2)
                    u_con = np.arccos(u_con_cosu)
                    v_con = np.arccos(vec_z)

                    if u_con_sinu < 0:
                        u_con = - u_con + 2.0 * np.pi # 0 <= u_con < 2*np.pi

                    if v_con == np.pi:
                        v_con = v_con - (np.pi / self.number_v) * 0.1
                    # here change pi into other value to avoid error in 
                    # classification
                    for m in np.arange(self.number_u):
                        if (u_con < 2 * np.pi / self.number_u * (m+1)):
                            for n in np.arange(self.number_v):
                                if (v_con < np.pi / self.number_v * (n+1)):
                                    self.dataArr[m,n] += 1
                                    self.dataArr[
                                    int(m + 1 + self.number_u/2)%self.number_u - 1, 
                                    int(self.number_v - n - 1)] += 1
                                    break
                            break
        self.fabTen /= c_count
        print(self.fabTen)

        self.anisoFabTen[:, :] = self.fabTen[:, :]
        for i in np.arange(3):
            self.anisoFabTen[i, i] -= 1.0/3.0


        self.invFabTen = 0.0
        for row in np.arange(3):
            for col in np.arange(3):
                self.invFabTen += self.anisoFabTen[row, col] ** 2

        self.invFabTen = np.sqrt(3.0/2.0 * self.invFabTen)


    def get_data_num_mech(self):
        "getting data from the contact list"
        self.dataArrMech = np.zeros([self.number_u, self.number_v])
        for ball in it.ball.list():
            if ball.contact_count() >= 2:
                for contact in ball.contacts():
                    # if contact.__class__ == it.BallBallContact:
                    force_vec = np.array(contact.force_global())
                    force = np.linalg.norm(force_vec)
                    direction_vec = np.array(contact.normal())
                    vec_x = direction_vec[0]
                    vec_y = direction_vec[1]
                    vec_z = direction_vec[2]
                    if (vec_x == 0.0) and (vec_y == 0.0):
                        self.dataArrMech[:,0] += 0.5 / self.number_u
                        self.dataArrMech[:,-1] += 0.5 /self.number_u
                    # here divide one contact to several 1/number to avoid
                    # valueException 'divided by zero' in cos(u)-calculation
                    else:
                        u_con_cosu = vec_x / \
                        np.sqrt(vec_x**2 + vec_y**2)
                        u_con_sinu = vec_y / \
                        np.sqrt(vec_x**2 + vec_y**2)
                        u_con = np.arccos(u_con_cosu)
                        v_con = np.arccos(vec_z)

                        if u_con_sinu < 0:
                            u_con = - u_con + 2.0 * np.pi # 0 <= u_con < 2*np.pi

                        if v_con == np.pi:
                            v_con = v_con - (np.pi / self.number_v) * 0.1
                        # here change pi into other value to avoid error in 
                        # classification
                        for m in np.arange(self.number_u):
                            if (u_con < 2 * np.pi / self.number_u * (m+1)):
                                for n in np.arange(self.number_v):
                                    if (v_con < np.pi / self.number_v * (n+1)):
                                        self.dataArrMech[m,n] += 0.5
                                        self.dataArrMech[
                                        int(m + 1 + self.number_u/2)%self.number_u - 1, 
                                        int(self.number_v - n - 1)] += 0.5
                                        break
                                break

    def get_data_den(self):
        self.dataArrDen = np.zeros([self.number_u, self.number_v])
        for n in np.arange(self.number_v):
            k = 2 * np.pi / self.number_u
            n1 = n * np.pi / self.number_v
            n2 = n1 + np.pi / self.number_v
            area = k * (np.cos(n1) - np.cos(n2))
            self.dataArrDen[:,n] = self.dataArr[:,n] / area

    def get_data_den_mech(self):
        self.dataArrDenMech = np.zeros([self.number_u, self.number_v])
        for n in np.arange(self.number_v):
            k = 2 * np.pi / self.number_u
            n1 = n * np.pi / self.number_v
            n2 = n1 + np.pi / self.number_v
            area = k * (np.cos(n1) - np.cos(n2))
            self.dataArrDenMech[:,n] = self.dataArrMech[:,n] / area

    def normalize(self):
        "let the maximum density be 1"
        "create a color map where minimum value cooresponds to 0 \
        while maximum value corresponds to 1"
        
        self.color_map = (self.dataArrDen - self.dataArrDen.min())/\
        (self.dataArrDen.max() - self.dataArrDen.min())

    def normalize_mech(self):
        "let the maximum density be 1"
        "create a color map where minimum value cooresponds to 0 \
        while maximum value corresponds to 1"

        self.density_maxMech = self.dataArrDenMech.max()
        self.density_minMech = self.dataArrDenMech.min()
        self.color_mapMech = (self.dataArrDenMech - self.density_minMech)/\
        (self.density_maxMech - self.density_minMech)

    def save_dis(self, number_u=36, number_v=18,):
        self.number_u = number_u
        self.number_v = number_v
        with open(self.file_n,"a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(np.arange(
                self.number_u*self.number_v*2))
        with open('invFabTen.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['invFabTen'])
        for time in np.linspace(0, 5.40, 541):
            it.command("model restore 'shear_time_{}'".format(round(time, 2)))
            self.get_data_num()
            self.get_data_den()
            self.normalize()
            with open(self.file_n,"a",newline="") as file:
                writer = csv.writer(file)
                arrConcatenated = np.concatenate([
                    self.dataArrDen,self.color_map])
                dataWritten = arrConcatenated.reshape(
                    self.number_u*self.number_v*2)
                writer.writerow(dataWritten)
            self.write_invFabTen()
            # self.write_title(round(index, 3))
            # self.write_data(round(index, 3))
                
    def write_title(self, time):
        with open('ball_info_shear{}.csv'.format(time), 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['pos_x', 'pos_y', 'pos_z', 'radius', 'disp_x', 
                'disp_y', 'disp_z', 'vel_x', 'vel_y', 'vel_z'])
        with open('wall_info_shear{}.csv'.format(time), 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['vertex_x', 'vertex_y', 'vertex_z'])



    def write_data(self, time):
        with open('ball_info_shear{}.csv'.format(time), 'a', newline='') as file:
            writer = csv.writer(file)
            for ball in it.ball.list():
                writer.writerow([ball.pos_x(), ball.pos_y(), ball.pos_z(), 
                    ball.radius(), ball.disp_x(), ball.disp_y(), ball.disp_z(), 
                    ball.vel_x(), ball.vel_y(), ball.vel_z()])
        with open('wall_info_shear{}.csv'.format(time), 'a', newline='') as file:
            writer = csv.writer(file)
            for facet in it.wall.facet.list():
                for vert in facet.vertices():
                    writer.writerow(np.array(vert.pos()))

    def write_invFabTen(self):
        with open('invFabTen.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.invFabTen])


    def get_info(self):
        for time in np.linspace(0, 1.37, 138):
            time = round(time,2)
            # state_name = 'deposition_loop_{}'.format(round(time, 3))
            state_name = 'shear_time_{}'.format(time)
            it.command("model restore '{}'".format(state_name))
            self.write_title(time)
            self.write_data(time)

    def save_dis_mech(self, number_u=36, number_v=18,):
        self.number_u = number_u
        self.number_v = number_v
        with open(self.file_nMech,"a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(np.arange(
                self.number_u*self.number_v*2))
        for time in np.linspace(0, 4.20, 421):
            it.command("model restore 'shear_time_{}'".format(round(time, 2)))
            self.get_data_num_mech()
            self.get_data_den_mech()
            self.normalize_mech()
            with open(self.file_nMech,"a",newline="") as file:
                writer = csv.writer(file)
                arrConcatenated = np.concatenate([
                    self.dataArrDenMech,self.color_mapMech])
                dataWritten = arrConcatenated.reshape(
                    self.number_u*self.number_v*2)
                writer.writerow(dataWritten)

    def save_skt(self):
        starts_x = []
        starts_y = []
        starts_z = []
        ends_x = []
        ends_y = []
        ends_z = []
        forces_scalar = []
        for contact in it.contact.list():
            if contact.__class__ == it.BallBallContact:
                center = contact.pos()
                b1 = contact.end1()
                b2 = contact.end2()
                force_scalar = np.linalg.norm(contact.force_global())
                force_dir = contact.force_global() / force_scalar
                start = center - force_dir*b1.radius()
                end = center + force_dir*b2.radius()
                starts_x.append(start[0])
                starts_y.append(start[1])
                starts_z.append(start[2])
                ends_x.append(end[0])
                ends_y.append(end[1])
                ends_z.append(end[2])
                forces_scalar.append(force_scalar)

        with open(self.skt_file_n,"a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "start_x","start_y","start_z",
                "end_x","end_y","end_z","force_scalar"])
            for start_x, start_y, start_z,\
            end_x, end_y, end_z, force_scalar in \
            zip(starts_x, starts_y, starts_z,\
                ends_x, ends_y, ends_z, forces_scalar):
                writer.writerow([start_x,start_y,start_z,
                    end_x,end_y,end_z,force_scalar])

    def save_sktMech(self):
        starts_x = []
        starts_y = []
        starts_z = []
        ends_x = []
        ends_y = []
        ends_z = []
        forces_scalar = []
        self.get_ave_force()
        for contact in it.contact.list():
            if contact.__class__ == it.BallBallContact:
                force_scalar = np.linalg.norm(contact.force_global())
                if force_scalar >= self.ave_force:
                    center = contact.pos()
                    b1 = contact.end1()
                    b2 = contact.end2()
                    force_dir = contact.force_global() / force_scalar
                    start = center - force_dir*b1.radius()
                    end = center + force_dir*b2.radius()
                    starts_x.append(start[0])
                    starts_y.append(start[1])
                    starts_z.append(start[2])
                    ends_x.append(end[0])
                    ends_y.append(end[1])
                    ends_z.append(end[2])
                    forces_scalar.append(force_scalar)

        with open(self.skt_file_nMech,"a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "start_x","start_y","start_z",
                "end_x","end_y","end_z","force_scalar"])
            for start_x, start_y, start_z,\
            end_x, end_y, end_z, force_scalar in \
            zip(starts_x, starts_y, starts_z,\
                ends_x, ends_y, ends_z, forces_scalar):
                writer.writerow([start_x,start_y,start_z,
                    end_x,end_y,end_z,force_scalar])
        